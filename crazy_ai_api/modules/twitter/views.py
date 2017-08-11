from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
import json
import twitter
from twitter import TwitterError

from .serializers import TweetSerializer

# Create your views here.


class ListTweets(APIView):

    def get(self, request, query):
        # http://127.0.0.1:8000/api/v1/tweets/(thing to look for)/
        api = twitter.Api(
            base_url='https://api.twitter.com/1.1',
            consumer_key='QmMcxaV3mA4pkxiUFtCk5gu85',
            consumer_secret='maFDNkP0W7NICOR77qzB4Fzwz2M4SJNa10KJgt7ovqPJBqSsg0',
            access_token_key='2547825031-TWh0iKBPDA1LyRlc471ypxTBVyoEfKtCyAnUC79',
            access_token_secret='kF2yOMYDB5b1MXNFidOZy5QVkkIIsQ1OuqPZfcCiuCClN',
        )

        results = api.GetSearch(
            raw_query="q=" + query)

        data = []
        for stat in results:
            data.append(stat._json)

        return Response(data, status=status.HTTP_200_OK)
        # return Response(results[0]._json,status=status.HTTP_200_OK)
