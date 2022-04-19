"""Example of using API4AI masks detection."""
import asyncio
import sys

import aiohttp


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


async def main():
    """Entry point."""
    image = sys.argv[1] if len(sys.argv) > 1 else 'https://storage.googleapis.com/api4ai-static/samples/med-mask-1.jpg'  # noqa

    # response = None
    async with aiohttp.ClientSession() as session:
        if '://' in image:
            # Data from image URL.
            data = {'url': image}
        else:
            # Data from local image file.
            data = {'image': open(image, 'rb')}
        # Make request.
        async with session.post(OPTIONS[MODE]['url'],
                                data=data,  # noqa
                                headers=OPTIONS[MODE]['headers']) as response:
            resp_json = await response.json()
            resp_text = await response.text()

        # Print raw response.
        print(f'💬 Raw response:\n{resp_text}\n')

        # Get mask data from objects.
        mask_data = [
            ent for obj in resp_json['results'][0]['entities'][0]['objects']
            for ent in obj['entities'] if ent['name'] == 'med-mask']

        with_mask_count = len([x for x in mask_data
                               if x['classes']['mask'] > x['classes']['nomask']])  # noqa

        print(f'💬 Total people found: {len(mask_data)}')
        print(f'💬 With mask: {with_mask_count}')
        print(f'💬 Without mask: {len(mask_data) - with_mask_count}')


if __name__ == '__main__':
    # Parse args.
    asyncio.run(main())
