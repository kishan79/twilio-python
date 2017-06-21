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


class OriginationUrlTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(MockResponse(500, ''))

        with self.assertRaises(TwilioException):
            self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                   .origination_urls(sid="OUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OriginationUrls/OUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(MockResponse(
            200,
            '''
            {
                "weight": 1,
                "date_updated": "2015-01-02T11:23:45Z",
                "enabled": true,
                "friendly_name": "friendly_name",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "priority": 1,
                "sip_url": "sip://sip-box.com:1234",
                "sid": "OUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-01-02T11:23:45Z",
                "trunk_sid": "TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "url": "https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OriginationUrls/OUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                        .origination_urls(sid="OUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(MockResponse(500, ''))

        with self.assertRaises(TwilioException):
            self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                   .origination_urls(sid="OUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OriginationUrls/OUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        ))

    def test_delete_response(self):
        self.holodeck.mock(MockResponse(
            204,
            ''
        ))

        actual = self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                        .origination_urls(sid="OUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").delete()

        self.assertTrue(actual)

    def test_create_request(self):
        self.holodeck.mock(MockResponse(500, ''))

        with self.assertRaises(TwilioException):
            self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                   .origination_urls.create(weight=1, priority=1, enabled=True, friendly_name="friendly_name", sip_url="https://example.com")

        values = {
            'Weight': 1,
            'Priority': 1,
            'Enabled': True,
            'FriendlyName': "friendly_name",
            'SipUrl': "https://example.com",
        }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OriginationUrls',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(MockResponse(
            201,
            '''
            {
                "weight": 1,
                "date_updated": "2015-01-02T11:23:45Z",
                "enabled": true,
                "friendly_name": "friendly_name",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "priority": 1,
                "sip_url": "sip://sip-box.com:1234",
                "sid": "OUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-01-02T11:23:45Z",
                "trunk_sid": "TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "url": "https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OriginationUrls/OUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                        .origination_urls.create(weight=1, priority=1, enabled=True, friendly_name="friendly_name", sip_url="https://example.com")

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(MockResponse(500, ''))

        with self.assertRaises(TwilioException):
            self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                   .origination_urls.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OriginationUrls',
        ))

    def test_read_full_response(self):
        self.holodeck.mock(MockResponse(
            200,
            '''
            {
                "meta": {
                    "first_page_url": "https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OriginationUrls?PageSize=1&Page=0",
                    "key": "origination_urls",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 1,
                    "previous_page_url": null,
                    "url": "https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OriginationUrls?PageSize=1&Page=0"
                },
                "origination_urls": [
                    {
                        "weight": 1,
                        "date_updated": "2015-01-02T11:23:45Z",
                        "enabled": true,
                        "friendly_name": "friendly_name",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "priority": 1,
                        "sip_url": "sip://sip-box.com:1234",
                        "sid": "OUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "2015-01-02T11:23:45Z",
                        "trunk_sid": "TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "url": "https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OriginationUrls/OUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ]
            }
            '''
        ))

        actual = self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                        .origination_urls.list()

        self.assertIsNotNone(actual)

    def test_read_empty_response(self):
        self.holodeck.mock(MockResponse(
            200,
            '''
            {
                "meta": {
                    "first_page_url": "https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OriginationUrls?PageSize=1&Page=0",
                    "key": "origination_urls",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 1,
                    "previous_page_url": null,
                    "url": "https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OriginationUrls?PageSize=1&Page=0"
                },
                "origination_urls": []
            }
            '''
        ))

        actual = self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                        .origination_urls.list()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(MockResponse(500, ''))

        with self.assertRaises(TwilioException):
            self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                   .origination_urls(sid="OUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OriginationUrls/OUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        ))

    def test_update_response(self):
        self.holodeck.mock(MockResponse(
            200,
            '''
            {
                "weight": 2,
                "date_updated": "2015-01-02T11:23:45Z",
                "enabled": false,
                "friendly_name": "updated_name",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "priority": 2,
                "sip_url": "sip://sip-updated.com:4321",
                "sid": "OUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-01-02T11:23:45Z",
                "trunk_sid": "TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "url": "https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OriginationUrls/OUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                        .origination_urls(sid="OUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").update()

        self.assertIsNotNone(actual)
