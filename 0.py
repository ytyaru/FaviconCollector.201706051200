import urllib.parse
#url = 'https://qiita.com'
#url = 'https://qiita.com/aaaaaa'
url = 'https://qiita.com/aaaaaa/'
u = urllib.parse.urlparse(url)
print(u)
print(urllib.parse.urlunparse(u))
print(urllib.parse.urlunparse(u).replace(u.path, ''))
#if '/' == u.path:
#    return urllib.parse.urlunparse(u)[:-1] # URL末尾の/削除

# 変換前                       変換後
# https://qiita.com         https://qiita.com
# https://qiita.com/        https:qiita.com
# https://qiita.com/aaaa    https://qiita.com
# https://qiita.com/aaaa/    https://qiita.com
# なぜかドメイン名のみで末尾に/があるパターンだとURLが壊れる。
# python3.4.3のときは問題なかったが、3.6.1で発生。バグ？仕様？
