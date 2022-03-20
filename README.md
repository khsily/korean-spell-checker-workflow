# Korean Spell Checker Workflow for Alfred4

Alfred에서 네이버 맞춤법 검사기를 사용하여 맞춤법 검사를 할 수 있게 해주는 workflow입니다.

## Install workflow
`Korean Spell Checker.workflow`를 다운받아서 실행합니다.

## Usage
```
sc [text]
```
![sample](./%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-09-12%20%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB%2010.45.05.png)


## Trouble Shooting
macos가 12.3으로 업데이트 됨에 따라 python2가 제거되었습니다.
따라서, Alfred공식 문서에 올라온 방법을 토대로 python2를 다시 설치해줘야 합니다.
https://www.alfredapp.com/help/kb/python-2-monterey/

```bash
export PATH="/opt/homebrew/bin:/usr/local/bin:${PATH}"
eval "$(brew shellenv)"
brew install pyenv
pyenv install 2.7.18
ln -s "${HOME}/.pyenv/versions/2.7.18/bin/python2.7" "${HOMEBREW_PREFIX}/bin/python"
```
