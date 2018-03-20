from subprocess import call

def enter_dns_file():  # 1
    with open('output/CNAME', 'w') as f:
        f.write('teguhwijaya.com')


def github(publish_drafts=False): # 2

    try:  # 3
        if os.path.exists('output/drafts'):
            if not publish_drafts:
                call('rm -rf output/drafts', shell=True)
    except Exception:
        pass

    call('ghp-import output', shell=True)  # 4
    call('git push '
          'git@github.com:jaycode/jaycode.github.io.git '
          'gh-pages:master -f', shell=True) # 5
    # call('rm -rf output', shell=True)  # 6


if __name__ == '__main__':
    call('pelican content', shell=True)
    enter_dns_file()
    github()