#!/bin/bash

######################################################
# NOTE:                                              #
#   This script requires "jq" command line tool!     #
#   See https://stedolan.github.io/jq/               #
######################################################


IMAGE=${1}
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Run base sample script to get raw output.
raw_response=$(bash ${DIR}/sample.sh "${IMAGE}")
echo -e "💬 Raw response:\n${raw_response}\n"

# Get mask data from objects.
total=$(jq ".results[0].entities[0].objects | length" <<< ${raw_response})
masks=$(jq "[.results[0].entities[0].objects[].entities[1].classes  | select (.mask > .nomask)] | length" <<< ${raw_response})
let nomasks=$total-$masks
echo "💬 Total people found: ${total}"
echo "💬 With mask: ${masks}"
echo "💬 Without mask: ${nomasks}"
