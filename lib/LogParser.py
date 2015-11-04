# -*- coding: utf-8 -*-

__author__ = 'ruggero'

import re
import logging

from lib.Errors import MalformedLogRowError


class LogParser(object):
    path_to_log_file = None

    def __init__(self, path_to_log_file):
        self.path_to_log_file = path_to_log_file

    def parse(self):
        """
        Parse a log file, yielding a LogRow object per each row.
        """
        with open(self.path_to_log_file, 'r') as fh:
            for row in fh:
                try:
                    log_row = LogRow(row)
                    yield log_row

                except MalformedLogRowError:
                    logging.error('Invalid row: {}'.format(row))
                    pass


class LogRow(object):
    def __init__(self, row):
        self.row = row
        self.parse_row(row)

    def parse_row(self, row):
        """
        Parse a log row, validating it against a regexp
        and extracting all the pieces of information.
        :param row: the row to parse
        :type row: str
        :raise MalformedLogRowError:
        """
        match = re.match(r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(.+)\] "(.*)" (\d+) (\d+) "(.*)" "(.*)"$', row)
        if match is None:
            raise MalformedLogRowError

        self.ip_address, \
        self.request_time_in, \
        request, \
        status_code, \
        response_size, \
        self.referrer, \
        self.user_agent = match.groups()

        self.request_method, self.request, self.request_protocol = request.split(' ')
        self.status_code = int(status_code)
        self.response_size = int(response_size)
        self.top_level_dir = self.request.split('/')[1]

    def is_off_site(self):
        """
        Tell whether a specific row represents an off-site request.
        :rtype bool:
        """
        return re.match(r'^https?://.*\.example\.com/', self.referrer) is None

    def is_2xx_response(self):
        """
        Tell whether the response has been returned successfully.
        :return bool:
        """
        return 200 <= self.status_code < 300

    def get_customer(self):
        """
        Return the customer name (ie: the top level request directory).
        :rtype str:
        """
        return self.top_level_dir
