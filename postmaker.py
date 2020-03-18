"""
Quick simple script to create post boilerplate.

run: python postmaker.py "post name" -c "category1, category2, etc."
"""

import argparse
from urllib import parse
import datetime

POSTS_LOCATION = '_posts/'
HEADER_STRING = '---\nlayout: page\ntitle: "{title}"\ndate: {date} -0000\ncategories: {categories}\n---\n'

def prepare_url(postname):
    convert_spaces = postname.replace(" ", "_")
    remove_apost = convert_spaces.replace("'", "")
    remove_comma = remove_apost.replace(",", "")
    url_friendly = parse.quote_plus(remove_comma)
    return url_friendly

def save_new_post(postname, categories=None):
    now = datetime.datetime.now()
    url_friendly = prepare_url(postname)
    filedate = now.strftime("%Y-%m-%d-")
    filename = POSTS_LOCATION + filedate + url_friendly + ".md"
    
    header_date = now.strftime("%Y-%m-%d %H:%M:%S")
    header = HEADER_STRING.format(title=postname,date=header_date, categories=categories)
    with open(filename, 'w') as f:
        f.write(header)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create post boilerplate in _posts')
    parser.add_argument('postname', type=str,
                        help='a name for the post')
    parser.add_argument('--category', 
                        help='sum the integers (default: find the max)')
    args = parser.parse_args()
    save_new_post(args.postname, args.category)

