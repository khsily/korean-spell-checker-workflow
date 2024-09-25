# -*- coding: utf-8 -*-

import sys
from workflow import Workflow, web
import re
from urllib.parse import unquote


def get_passport_key():
    url = "https://m.search.naver.com/search.naver"
    params = dict(
        where="nexearch",
        query="맞춤법검사기",
    )

    r = web.get(url, params)
    match = re.search(r"passportKey=(.*?)\"", r.text).group(1)
    return unquote(unquote(match))


def get_data(query):
    passport_key = get_passport_key()
    url = "https://m.search.naver.com/p/csearch/ocontent/util/SpellerProxy"

    params = dict(
        where="nexearch",
        color_blindness=0,
        q=query,
        passportKey=passport_key,
    )

    r = web.get(url, params)
    r.raise_for_status()
    return r.json()


def main(wf):
    args = wf.args[0]

    def wrapper():
        return get_data(args)

    data = wf.cached_data(args, wrapper, max_age=30)
    data = data["message"]["result"]["notag_html"]

    wf.add_item(
        title="Check spelling for '%s'" % args,
        subtitle=data,
        autocomplete=data,
        arg=data,
        valid=True,
    )

    wf.send_feedback()


if __name__ == "__main__":
    wf = Workflow()
    sys.exit(wf.run(main))
