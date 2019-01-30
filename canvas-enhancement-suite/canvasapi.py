#!/usr/bin/env python3
#
# A Python script to:
# - interact directly with Canvis API
# - pass API calls to other modules
#
import requests
import argparse


args = argparse.ArgumentParser(description="A Python script for interacting with the Canvas LMS API.")
args.add_argument('api_key', type='str',
                  help='Canvas API key. Can be generated in Canvas settings.')
args.add_argument('-u','--url', type='str',
                  help="Your institution's Canvas base URL (defaults to unt.instructure.com")
if __name__ == "__main__": main()