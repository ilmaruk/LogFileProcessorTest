# -*- coding: utf-8 -*-

__author__ = 'ruggero'

import operator


class StatsManager(object):
    def __init__(self):
        self.total_requests = 0
        self.off_site_requests = 0
        self.requests_per_url = dict()
        self.usage_per_client = dict()

    def increment_total_requests(self):
        """
        Increment the total number of requests.
        """
        self.total_requests += 1

    def increment_off_site_requests(self):
        """
        Increment the total number of off-line requests.
        """
        self.off_site_requests += 1

    def update_url_requests_counter(self, url):
        """
        Update the counter of requests against a specific URL.
        :param url: the requested URL
        :type url: str
        """
        try:
            self.requests_per_url[url] += 1

        except KeyError:
            # In case the key didn't exist
            self.requests_per_url[url] = 1

    def update_customer_usage(self, customer, usage):
        """
        Update the usage (bytes) for a specific customer.
        :param customer: the customer
        :type customer: str
        :param usage: the usage (bytes) of the current request
        :type usage: int
        """
        try:
            self.usage_per_client[customer] += usage

        except KeyError:
            # In case the key didn't exist
            self.usage_per_client[customer] = usage

    def print_off_site_stats(self):
        percentage = 1.0 if self.total_requests == 0 else float(self.off_site_requests) / float(self.total_requests)
        print 'Off-site requests: {offsite:d} of {total:d} ({percentage:.2f}%)'.format(
            offsite=self.off_site_requests,
            total=self.total_requests,
            percentage=percentage * 100.0
        )

    def print_top_urls_stats(self, limit=10):
        sorted_urls = sorted(self.requests_per_url.items(), key=operator.itemgetter(1), reverse=True)
        print 'Top {limit:d} URLs:'.format(limit=limit)
        for url, count in sorted_urls[0:9]:
            print '{count:>13d} - {url:s}'.format(
                count=count,
                url=url
            )

    def print_customer_usage_stats(self):
        print 'Customer usage summary:'
        for customer, usage in self.usage_per_client.items():
            print '{usage:>10.2f} GB - {customer:s}'.format(
                usage=float(usage / 1000000000.0),
                customer=customer
            )

