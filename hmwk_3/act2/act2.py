#!/usr/bin/env python

#
# Name: Simon Buchheit
# Date: October 6, 2019
#
# CSEC-380 : hmwk3 : Act2
#
# Purpose: This script crawls the site: www.rit.edu
#          to a depth of 4. On each page emails are harvested
#          and saved.
#

import simplerequest


def main():

    # God damn... I hate this one

    simplerequest.new_crawl("rit.edu")


if __name__ == "__main__":
    main()
