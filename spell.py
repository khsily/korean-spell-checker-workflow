import sys
from workflow import Workflow, web


def get_data(query):
    url = 'https://m.search.naver.com/p/csearch/ocontent/util/SpellerProxy'

    params = dict(
        where='nexearch',
        color_blindness=0,
        q=query,
    )

    r = web.get(url, params)
    r.raise_for_status()
    return r.json()


def main(wf):
    args = wf.args[0]

    def wrapper():
        return get_data(args)

    data = wf.cached_data(args, wrapper, max_age=30)
    data = data['message']['result']['notag_html']

    wf.add_item(
        title='Check spelling for \'%s\'' % args,
        subtitle=data,
        autocomplete=data,
        arg=data,
        valid=True
    )

    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
