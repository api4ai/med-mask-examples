# API4AI masks detection sample

This directory contains a minimalistic sample that sends requests to the API4AI Masks Detection API.
The sample is implemented `nodejs` using [axios](https://www.npmjs.com/package/axios) and [from-data](https://www.npmjs.com/package/form-data) packages.


## Overview

High-accuracy solution for medical masks detection. This solution analyzes a given image, detects people in it and reports if they wear protective masks or not.


## Getting started

*NodeJS version `8.3.0` or greater is required to run this script.*

Preinstall dependencies before use:

```bash
npm i --production
```

Try sample with default args:

```bash
node index.js
```

Try sample with your local image:

```bash
node index.js image.jpg
```


## About API keys

This demo by default sends requests to free endpoint at `demo.api4ai.cloud`.
Demo endpoint is rate limited and should not be used in real projects.

Use [RapidAPI marketplace](https://rapidapi.com/api4ai-api4ai-default/api/masks-detection/details) to get the API key. The marketplace offers both
free and paid subscriptions.

[Contact us](https://api4.ai/contacts?utm_source=med_maskexample_repo&utm_medium=readme&utm_campaign=examples) in case of any questions or to request a custom pricing plan
that better meets your business requirements.


## Links

* 📩 Email: hello@api4.ai
* 🔗 Website: [http://api4.ai](https://api4.ai?utm_source=med_maskexample_repo&utm_medium=readme&utm_campaign=examples)
* 🤖 Telegram demo bot: https://t.me/a4a_face_masks_detection_bot
* 🔵 Our API at RapidAPI marketplace: https://rapidapi.com/api4ai-api4ai-default/api/masks-detection/details
