# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import (
    IntegrationTestCase,
    MockResponse,
)
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class MobileTestCase(IntegrationTestCase):

    def test_list_request(self):
        self.holodeck.mock(MockResponse(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .incoming_phone_numbers \
                                 .mobile.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/Mobile.json',
        ))

    def test_read_full_response(self):
        self.holodeck.mock(MockResponse(
            200,
            '''
            {
                "end": 0,
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/Mobile.json?Page=0&PageSize=50",
                "incoming_phone_numbers": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "address_requirements": "none",
                        "api_version": "2010-04-01",
                        "beta": null,
                        "capabilities": {
                            "mms": false,
                            "sms": true,
                            "voice": false
                        },
                        "date_created": "Tue, 08 Sep 2015 16:21:16 +0000",
                        "date_updated": "Tue, 08 Sep 2015 16:21:16 +0000",
                        "friendly_name": "61429099450",
                        "phone_number": "+61429099450",
                        "origin": "origin",
                        "sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "sms_application_sid": "",
                        "sms_fallback_method": "POST",
                        "sms_fallback_url": "",
                        "sms_method": "POST",
                        "sms_url": "",
                        "status_callback": "",
                        "status_callback_method": "POST",
                        "trunk_sid": null,
                        "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
                        "voice_application_sid": "",
                        "voice_caller_id_lookup": false,
                        "voice_fallback_method": "POST",
                        "voice_fallback_url": null,
                        "voice_method": "POST",
                        "voice_url": null
                    }
                ],
                "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/Mobile.json?Page=0&PageSize=50",
                "next_page_uri": null,
                "num_pages": 1,
                "page": 0,
                "page_size": 50,
                "previous_page_uri": null,
                "start": 0,
                "total": 1,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/Mobile.json"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .incoming_phone_numbers \
                                      .mobile.list()

        self.assertIsNotNone(actual)

    def test_read_empty_response(self):
        self.holodeck.mock(MockResponse(
            200,
            '''
            {
                "end": 0,
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/Mobile.json?Page=0&PageSize=50",
                "incoming_phone_numbers": [],
                "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/Mobile.json?Page=0&PageSize=50",
                "next_page_uri": null,
                "num_pages": 1,
                "page": 0,
                "page_size": 50,
                "previous_page_uri": null,
                "start": 0,
                "total": 1,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/Mobile.json"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .incoming_phone_numbers \
                                      .mobile.list()

        self.assertIsNotNone(actual)

    def test_create_request(self):
        self.holodeck.mock(MockResponse(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .incoming_phone_numbers \
                                 .mobile.create(phone_number="+987654321")

        values = {
            'PhoneNumber': "+987654321",
        }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/Mobile.json',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(MockResponse(
            201,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "address_requirements": "none",
                "api_version": "2010-04-01",
                "beta": false,
                "capabilities": {
                    "mms": true,
                    "sms": false,
                    "voice": true
                },
                "date_created": "Thu, 30 Jul 2015 23:19:04 +0000",
                "date_updated": "Thu, 30 Jul 2015 23:19:04 +0000",
                "friendly_name": "(808) 925-5327",
                "phone_number": "+18089255327",
                "origin": "origin",
                "sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sms_application_sid": "",
                "sms_fallback_method": "POST",
                "sms_fallback_url": "",
                "sms_method": "POST",
                "sms_url": "",
                "status_callback": "",
                "status_callback_method": "POST",
                "trunk_sid": null,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
                "voice_application_sid": "",
                "voice_caller_id_lookup": false,
                "voice_fallback_method": "POST",
                "voice_fallback_url": null,
                "voice_method": "POST",
                "voice_url": null
            }
            '''
        ))

        actual = self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .incoming_phone_numbers \
                                      .mobile.create(phone_number="+987654321")

        self.assertIsNotNone(actual)
