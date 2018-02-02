# Vanilla Python Scraper
## Introduction
This is a basic demonstartion on how a Python scraper(**not a crawler**) can extract key information from a target website. Some minor yet sophiscated challenges can be easily tackled, such as (1) turning over pages and (2) dealing with unstructured format of target information(i.e. prices).

## Aim
The target website is the official explorer website of Crypto Kitties (http://www.kittyexplorer.com/prices) where you can find information such as the prices of the kitties and other auxiliary items. The aim of this toy project is to iterate through all the pages and all the kitties on each page to extract and sum up the total prices of all kitties, in USD.

## Notes
The exact USD price can be found by clicking into the transaction hash `txhash` on the right side of each entry of kitties. The price in USD is listed as this example `Value: 0.005 Ether ($4.61)`. The scraper can find the number `4.61` and carry on to collect the price of the next kitty.