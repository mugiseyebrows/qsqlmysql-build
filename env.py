import argparse

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('tools', nargs='+', choices=['vc','qt5','jom','qwt','7z','git','python'])

    paths = {
        'vc': '',
        'qt5': 'C:\\Qt\\5.14.2\\msvc2017_64\\bin',
        'qwt': 'C:\\Qwt-6.2.0\\lib',
        '7z': 'C:\\Program Files\\7-Zip',
        'git': 'C:\\Program Files\\Git\\cmd',
        'python': 'C:\\Python39-x64;C:\\Python39-x64\\Scripts',
        'jom': 'C:\\Qt\\Tools\\QtCreator\\bin\\jom'
    }

    args = parser.parse_args()

    path = []
    cmds = []

    if 'vc' in args.tools:
        cmds.append('call "C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\VC\\Auxiliary\\Build\\vcvars64.bat"')

    for tool in args.tools:
        if paths[tool] != "":
            path.append(paths[tool])

    path.append('%PATH%')
    cmds.append('set PATH={}'.format(";".join(path)))

    with open('tmp.txt','w',encoding='utf-8') as f:
        f.write("\n".join(cmds) + "\n")

if __name__ == "__main__":
    main()
