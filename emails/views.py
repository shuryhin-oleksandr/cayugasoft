# -*- encoding: utf-8 -*-
import httplib2
from apiclient import errors
from apiclient.discovery import build
from oauth2client.client import AccessTokenCredentials
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response


def get_service(request):
    user = request.user
    social = user.social_auth.get(provider='google-oauth2')
    access_token = social.extra_data['access_token']

    credentials = AccessTokenCredentials(access_token, 'my-user-agent/1.0')
    http = httplib2.Http()
    http = credentials.authorize(http)
    service = build(serviceName='gmail', version='v1', http=http)

    return service


def get_email_snippet_list(service):
    response = service.users().messages().list(userId='me', maxResults=100, ).execute()

    messages = response.get('messages', [])
    message_ids = [message['id'] for message in messages]

    emails_snippets = [get_email_snippet(
        service=service, user_id='me', msg_id=message_id
        ) for message_id in message_ids]

    return emails_snippets


def get_email_snippet(service, user_id, msg_id):
    message = service.users().messages().get(userId=user_id, id=msg_id,).execute()
    return message['snippet']


class Emails(APIView):
    renderer_classes = (TemplateHTMLRenderer,)

    def get(self, request, format=None):
        # return Response(1)
        try:
            service = get_service(request)
            email_snippets = get_email_snippet_list(service)
            return Response({'email_snippets': email_snippets}, template_name='emails/index.html')
        except errors.HttpError, error:
            return Response('An error occurred: %s' % error)
        except:
            return Response({}, template_name='emails/index.html')
