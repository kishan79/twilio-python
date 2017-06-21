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


class DailyTestCase(IntegrationTestCase):

    def test_list_request(self):
        self.holodeck.mock(MockResponse(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .usage \
                                 .records \
                                 .daily.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Daily.json',
        ))

    def test_read_full_response(self):
        self.holodeck.mock(MockResponse(
            200,
            '''
            {
                "end": 0,
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Daily?Page=0&PageSize=1",
                "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Daily?Page=101843&PageSize=1",
                "next_page_uri": null,
                "num_pages": 101844,
                "page": 0,
                "page_size": 1,
                "previous_page_uri": null,
                "start": 0,
                "total": 101844,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Daily",
                "usage_records": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "api_version": "2010-04-01",
                        "category": "sms-inbound-shortcode",
                        "count": "0",
                        "count_unit": "messages",
                        "description": "Short Code Inbound SMS",
                        "end_date": "2015-09-06",
                        "price": "0",
                        "price_unit": "usd",
                        "start_date": "2015-09-06",
                        "subresource_uris": {
                            "all_time": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/AllTime.json?Category=sms-inbound-shortcode",
                            "daily": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Daily.json?Category=sms-inbound-shortcode",
                            "last_month": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/LastMonth.json?Category=sms-inbound-shortcode",
                            "monthly": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Monthly.json?Category=sms-inbound-shortcode",
                            "this_month": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/ThisMonth.json?Category=sms-inbound-shortcode",
                            "today": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Today.json?Category=sms-inbound-shortcode",
                            "yearly": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Yearly.json?Category=sms-inbound-shortcode",
                            "yesterday": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Yesterday.json?Category=sms-inbound-shortcode"
                        },
                        "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Daily?Category=sms-inbound-shortcode&StartDate=2015-09-06&EndDate=2015-09-06",
                        "usage": "0",
                        "usage_unit": "messages"
                    }
                ]
            }
            '''
        ))

        actual = self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .usage \
                                      .records \
                                      .daily.list()

        self.assertIsNotNone(actual)

    def test_read_empty_response(self):
        self.holodeck.mock(MockResponse(
            200,
            '''
            {
                "end": 0,
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Daily?Page=0&PageSize=1",
                "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Daily?Page=101843&PageSize=1",
                "next_page_uri": null,
                "num_pages": 101844,
                "page": 0,
                "page_size": 1,
                "previous_page_uri": null,
                "start": 0,
                "total": 101844,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Daily",
                "usage_records": []
            }
            '''
        ))

        actual = self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .usage \
                                      .records \
                                      .daily.list()

        self.assertIsNotNone(actual)
