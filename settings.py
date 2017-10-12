import os

# Amazon Access Codes
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', None)
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", None)
AWS_ASSOCIATE_TAG = os.environ.get("AWS_ASSOCIATE_TAG", None)

# Cookie Secret
cookie_secret = os.environ.get("cookie_secret", None)

# Database URLs
postgres_url = os.environ.get('postgres_url', None)
mongo_url = os.environ.get("mongo_url", None)

# Third Party API Keys
meaning_cloud_key = os.environ.get("meaning_cloud_key", None)
