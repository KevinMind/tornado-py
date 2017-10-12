import os

import bottlenose
from bs4 import BeautifulSoup
import lxml

import json

from settings import AWS_ACCESS_KEY_ID, AWS_ASSOCIATE_TAG, AWS_SECRET_ACCESS_KEY
key = AWS_ACCESS_KEY_ID
secret = AWS_SECRET_ACCESS_KEY
tag = AWS_ASSOCIATE_TAG


# generate response
def item_search(keywords):

    service = "AWSECommerceService"
    AWS_ACCESS_KEY_ID= key
    AWS_SECRET_ACCESS_KEY= secret
    AWS_ASSOCIATE_TAG = tag
    REGION = "US"

    # error handler
    def error_handler(err):
        ex = err['exception']
        return ex.response

    # define connection by account credentials
    amazon = bottlenose.Amazon(
        AWS_ACCESS_KEY_ID,
        AWS_SECRET_ACCESS_KEY,
        AWS_ASSOCIATE_TAG,
        Region = REGION
    )

    response = amazon.ItemSearch(
        Keywords= keywords,
        SearchIndex="All",
        ErrorHandler=error_handler,
        ResponseGroup="Images,ItemAttributes,Reviews"
    )
    print(response)
    items = []

    soup = BeautifulSoup(response, "xml")
    print(soup.TotalResults)

    find_items = soup.findAll("Item")

    for x in find_items:
        # generate a new item dictionary
        item = {}

        # test images
        print(x.SmallImage)
        if x.LargeImage.URL:
            image = x.LargeImage.URL.string
        elif x.MediumImage.URL:
            image = x.MediumImage.URL.string
        else:
            image = "https://d4n5pyzr6ibrc.cloudfront.net/media/27FB7F0C-9885-42A6-9E0C19C35242B5AC/4785B1C2-8734-405D-96DC23A6A32F256B/thul-90efb785-97af-5e51-94cf-503fc81b6940.jpg?response-content-disposition=inline"
        # add data to dict
        item['title'] = x.ItemAttributes.Title.string
        item['url'] = x.DetailPageURL.string
        item['asin'] = x.ASIN.string
        item['image'] = image
        if x.ItemAttributes.ItemDimensions:
            dimensions = []
            for dimension in x.ItemAttributes.ItemDimensions:
                dimensions.append(dimension)
            item['dimensions'] = dimensions
        if x.ItemAttributes.Brand:
            item['brand'] = x.ItemAttributes.Brand.string
        if x.ItemAttributes.ListPrice:
            item['price'] = x.ItemAttributes.ListPrice.FormattedPrice.string
        if x.ItemAttributes.CurrencyCode:
            item['currency'] = x.ItemAttributes.CurrencyCode.string
        if x.CustomerReviews:
            item['reviews'] = x.CustomerReviews.IFrameURL.string
        # debug
        # print(item)
        # add dict to list
        items.append(item)
    # print(items)
    return items


        # print("Title: {}\nLink: {}\nASIN: {}\nImage: {}\nDimensions: {}\nBrand: {}\nPrice: {}\nCurrency: {}\nReviews: {}\n\n\n".format(title, link, asin, image, dimensions, brand, price, currency, reviews) + ("x" * 20))
        # # print("Title: {}\nLink: {}\nItemASIN: {}\nimage: {}\nDimensions: {} x {} x {}\nBrand: {}\nPrice: {} CURRENCY: {}".format(title, link, asin, image, height, length, width, brand, price, currency))
