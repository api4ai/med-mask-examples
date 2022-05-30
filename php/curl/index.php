#!/usr/bin/env php

<?php
// Example of using API4AI masks detection.

// Use 'demo' mode just to try api4ai for free. Free demo is rate limited.
// For more details visit:
//   https://api4.ai

// Use 'rapidapi' if you want to try api4ai via RapidAPI marketplace.
// For more details visit:
//   https://rapidapi.com/api4ai-api4ai-default/api/masks-detection/details
$MODE = 'demo';

// Your RapidAPI key. Fill this variable with the proper value if you want
// to try api4ai via RapidAPI marketplace.
$RAPIDAPI_KEY = null;

$OPTIONS = [
    'demo' => [
        'url' => 'https://demo.api4ai.cloud/med-mask/v1/results',
        'headers' => ['A4A-CLIENT-APP-ID: sample']
    ],
    'rapidapi' => [
        'url' => 'https://masks-detection.p.rapidapi.com/v1/results',
        'headers' => ["X-RapidAPI-Key: {$RAPIDAPI_KEY}"]
    ]
];

// Initialize request session.
$request = curl_init();

// Check if path to local image provided.
$data = ['url' => 'https://storage.googleapis.com/api4ai-static/samples/med-mask-1.jpg'];
if (array_key_exists(1, $argv)) {
    if (strpos($argv[1], '://')) {
        $data = ['url' => $argv[1]];
    } else {
        $filename = pathinfo($argv[1])['filename'];
        $data = ['image' => new CURLFile($argv[1], null, $filename)];
    }
}

// Set request options.
curl_setopt($request, CURLOPT_URL, $OPTIONS[$MODE]['url']);
curl_setopt($request, CURLOPT_HTTPHEADER, $OPTIONS[$MODE]['headers']);
curl_setopt($request, CURLOPT_POST, true);
curl_setopt($request, CURLOPT_POSTFIELDS, $data);
curl_setopt($request, CURLOPT_RETURNTRANSFER, true);

// Execute request.
$result = curl_exec($request);

// Decode response.
$raw_response = json_decode($result, true);

// Print raw response.
echo join('',
          ["💬 Raw response:\n",
           json_encode($raw_response),
           "\n"]);

// Parse response and get mask data from objects.
$mask_data_count = count($raw_response['results'][0]['entities'][0]['objects']);
$with_mask_count = count(array_filter($raw_response['results'][0]['entities'][0]['objects'],
                                      'get_with_mask'));
$without_mask_count = $mask_data_count - $with_mask_count;

// Close request session.
curl_close($request);

// Print mask data.
echo join('',
          ["\n💬 Total people found: {$mask_data_count}",
           "\n💬 With mask: {$with_mask_count}",
           "\n💬 Without mask: {$without_mask_count}",
           "\n"]);

function get_with_mask(array $obj) {
    foreach ($obj['entities'] as $entity) {
        if ($entity['name'] === 'med-mask') {
            if ($entity['classes']['mask'] > $entity['classes']['nomask']) {
                return $obj;
            }
        }
    }
}
?>
