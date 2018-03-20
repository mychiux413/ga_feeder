import os, shutil, re
import easygui

def main():

    dirname = easygui.diropenbox()
    # print(dirname)
    with open('feed_in', 'r') as thefile:
        feed_in = thefile.read()

    def embedded_html(path, feed_in):
        with open(path, 'r') as thefile:
            out = thefile.read()
        feed_in = '\n'.join([' '*4 + line for line in feed_in.split('\n')])

        out = re.sub("</head>", feed_in + "\n</head>", out)
        return out


    dst_dir = dirname + '_out'

    if os.path.exists(dst_dir):
        print("out dir is exists, bypass!")
        return None
    shutil.copytree(src=dirname, dst=dst_dir)


    for walk in os.walk(dst_dir):
        files = walk[2]
        for fname in files:
            if fname.endswith('.html'):
                html_path = os.path.join(walk[0], fname)
                html = embedded_html(html_path, feed_in)
                with open(html_path, 'w') as thefile:
                    thefile.write(html)
    print('export at {}'.format(dst_dir))

if __name__ == '__main__':
    main()