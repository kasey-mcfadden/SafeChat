#!/bin/bash
source ~/.bash_profile
cd path/to/vine_in_chal
rm Archive.zip
zip -r Archive.zip *
aws lambda update-function-code --function-name Burner --zip-file fileb:///Users/kmcfadden2/Documents/GitHub/vine_in_chal/Archive.zip
