#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'ruggero'

import sys
from os import path, listdir
from os.path import isfile, join
from lib.StatsManager import StatsManager
from lib.LogParser import LogParser


def usage():
    print 'Usage: {} <log_files_dir>'.format(path.basename(__file__))


def main(log_files_dir):
    if not path.isdir(log_files_dir):
        print 'Error: {} is not a directory'.format(log_files_dir)
        usage()
        return 2

    stats_manager = StatsManager()

    try:
        # List all the file in the directory to scan
        log_files = [join(log_files_dir, log_file) for log_file in listdir(log_files_dir) if isfile(join(log_files_dir, log_file))]
    except OSError as os_error:
        print 'Error: {}'.format(str(os_error))
        usage()
        return 2

    # Per each file, parse its lines and update the stats
    for log_file in log_files:
        log_parser = LogParser(log_file)
        line = 0
        try:
            for log_row in log_parser.parse():
                line += 1
                stats_manager.increment_total_requests()
                if log_row.is_off_site():
                    stats_manager.increment_off_site_requests()

                if log_row.is_2xx_response():
                    stats_manager.update_url_requests_counter(log_row.request)

                stats_manager.update_customer_usage(log_row.get_customer(), log_row.response_size)
        except IOError as io_error:
            print 'Error: {}'.format(str(io_error))

    # Finally display stats
    stats_manager.print_off_site_stats()
    stats_manager.print_top_urls_stats()
    stats_manager.print_customer_usage_stats()

    return 0


if '__main__' == __name__:
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)

    sys.exit(main(sys.argv[1]))
