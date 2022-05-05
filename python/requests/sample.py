#!/usr/bin/env python3

"""Example of using API4AI masks detection."""

import mimetypes
import os
import sys

import requests


# Use 'demo' mode just to try api4ai for free. Free demo is rate limited.
# For more details visit:
#   https://api4.ai
#
# Use 'rapidapi' if you want to try api4ai via RapidAPI marketplace.
# For more details visit:
#   https://rapidapi.com/api4ai-api4ai-default/api/masks-detection/details
MODE = 'demo'


# Your RapidAPI key. Fill this variable with the proper value if you want
# to try api4ai via RapidAPI marketplace.
RAPIDAPI_KEY = ''


OPTIONS = {
    'demo': {
        'url': 'https://demo.api4ai.cloud/med-mask/v1/results',
        'headers': {'A4A-CLIENT-APP-ID': 'sample'}
    },
    'rapidapi': {
        'url': 'https://masks-detection.p.rapidapi.com/v1/results',
        'headers': {'X-RapidAPI-Key': RAPIDAPI_KEY}
    }
}


if __name__ == '__main__':
    # Parse args.
    image = sys.argv[1] if len(sys.argv) > 1 else 'https://storage.googleapis.com/api4ai-static/samples/med-mask-1.jpg'

    if '://' in image:
        # POST image via URL.
        response = requests.post(
            OPTIONS[MODE]['url'],
            headers=OPTIONS[MODE]['headers'],
            data={'url': image})
    else:
        # POST image as file.
        mt = mimetypes.guess_type(image)[0]
        with open(image, 'rb') as image_file:
            response = requests.post(
                OPTIONS[MODE]['url'],
                headers=OPTIONS[MODE]['headers'],
                files={'image': (os.path.basename(image), image_file, mt)}
            )

    print(f'💬 Raw response:\n{response.text}\n')

    # Get mask data from objects.
    mask_data = [
        ent for obj in response.json()['results'][0]['entities'][0]['objects']
        for ent in obj['entities'] if ent['name'] == 'med-mask']

    with_mask_count = len([x for x in mask_data
                           if x['classes']['mask'] > x['classes']['nomask']])

    print(f'💬 Total people found: {len(mask_data)}')
    print(f'💬 With mask: {with_mask_count}')
    print(f'💬 Without mask: {len(mask_data) - with_mask_count}')
