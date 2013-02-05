import os
import argparse


def get_default_style():
    return """
    ul{padding-left:3px}
    .file, .folder{margin-top:3px; background-repeat:no-repeat; list-style-type:none; padding-left:20px}
    .folder{background-image:url('data:image/png; base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABGdBTUEAAK/INwWK6QAAABl0RVh0U29mdHdhcmUAQWRvYmUgSW1hZ2VSZWFkeXHJZTwAAAGrSURBVDjLxZO7ihRBFIa/6u0ZW7GHBUV0UQQTZzd3QdhMQxOfwMRXEANBMNQX0MzAzFAwEzHwARbNFDdwEd31Mj3X7a6uOr9BtzNjYjKBJ6nicP7v3KqcJFaxhBVtZUAK8OHlld2st7Xl3DJPVONP+zEUV4HqL5UDYHr5xvuQAjgl/Qs7TzvOOVAjxjlC+ePSwe6DfbVegLVuT4r14eTr6zvA8xSAoBLzx6pvj4l+DZIezuVkG9fY2H7YRQIMZIBwycmzH1/s3F8AapfIPNF3kQk7+kw9PWBy+IZOdg5Ug3mkAATy/t0usovzGeCUWTjCz0B+Sj0ekfdvkZ3abBv+U4GaCtJ1iEm6ANQJ6fEzrG/engcKw/wXQvEKxSEKQxRGKE7Izt+DSiwBJMUSm71rguMYhQKrBygOIRStf4TiFFRBvbRGKiQLWP29yRSHKBTtfdBmHs0BUpgvtgF4yRFR+NUKi0XZcYjCeCG2smkzLAHkbRBmP0/Uk26O5YnUActBp1GsAI+S5nRJJJal5K1aAMrq0d6Tm9uI6zjyf75dAe6tx/SsWeD//o2/Ab6IH3/h25pOAAAAAElFTkSuQmCC'); font-weight:bold}
    .file{background-image:url('data:image/png; base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAQAAAC1+jfqAAAABGdBTUEAAK/INwWK6QAAABl0RVh0U29mdHdhcmUAQWRvYmUgSW1hZ2VSZWFkeXHJZTwAAAC4SURBVCjPdZFbDsIgEEWnrsMm7oGGfZrohxvU+Iq1TyjU60Bf1pac4Yc5YS4ZAtGWBMk/drQBOVwJlZrWYkLhsB8UV9K0BUrPGy9cWbng2CtEEUmLGppPjRwpbixUKHBiZRS0p+ZGhvs4irNEvWD8heHpbsyDXznPhYFOyTjJc13olIqzZCHBouE0FRMUjA+s1gTjaRgVFpqRwC8mfoXPPEVPS7LbRaJL2y7bOifRCTEli3U7BMWgLzKlW/CuebZPAAAAAElFTkSuQmCC'); font-weight:normal}
    """


def plant_tree(starting_dir):
    print("<!doctype html>")
    print("<style>%s</style>" % get_default_style())
    print("<div class='dirdiv'>")
    print("<strong>%s</strong>" % starting_dir)
    print("<hr>")
    print("<ul>")

    walk(starting_dir)

    print("</div>")


def walk(dir):
    for item in os.listdir(dir):
        full_path = os.path.normpath(os.path.join(dir, item))
        indent = "  " * full_path[len(str(path)):].count("\\")
        if os.path.isdir(full_path):
            print("%s<li class='folder'>%s" % (indent, item))
            if len(os.listdir(full_path)) > 0:
                print("%s<ul>" % indent)
            else:
                print("</li>")

            walk(full_path)
        else:
            print("%s<li class='file'>%s</li>" % (indent, item))

        if item == os.listdir(dir)[-1:][0]:
            if os.path.isdir(full_path):
                print("%s</ul>" % indent[:-1])
            else:
                print("%s</ul>" % indent[:-1])
                print("%s</li>" % indent[:-1])

parser = argparse.ArgumentParser(description='Generate a simple HTML document \
                                                representing the hierarchy of \
                                                file and folders in the given \
                                                directory.')
parser.add_argument('dir', type=str, default='.',
                   help='Path to directory for generating HTML')
args = parser.parse_args()

dir = os.path.dirname(__file__)
path = os.path.abspath(os.path.join(dir, args.dir))
path = os.path.normcase(path)

if not os.path.exists(path):
    parser.error("The path %s does not exist." % path)

if not os.path.isdir(path):
    parser.error("The path %s is not a directory" % path)

plant_tree(path)
