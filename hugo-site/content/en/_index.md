---
title: Linux Console Fonts Screenshots
summary: An organized gallery of Linux console fonts screenshots
type: docs
---


## Introduction

ArchLinux’s [wiki page on console fonts](https://wiki.archlinux.org/title/Linux_console#Fonts)
is lacking an organized library of images available for previewing
and the wiki policy does not allow uploading images.
So I wrote a Python script
to produce a PNG image of all fonts contained in `/usr/share/kbd/consolefonts`.
Then I wrote an Ansible playbook to generate this site using
[Docsy](https://www.docsy.dev/).

Here is a tarball of the images&nbsp;:
[consolefonts-screenshots.tar.gz]({{% baseurl %}}files/consolefonts-screenshots.tar.gz)
(1.4&nbsp;MB).
It expands to a “consolefonts-screenshots” directory containing the same ~210 PNG files as below.

Please send any comments, suggestions or questions to
[alexandre@deverteuil.net](mailto:alexandre@deverteuil.net).


## Links

* The code for this site is at [github.com/adeverteuil/linux-console-fonts-screenshots](https://github.com/adeverteuil/linux-console-fonts-screenshots).
* My personal blog is at [alexandre.deverteuil.net](https://alexandre.deverteuil.net/).


## Readme files

For convenience, here are the readme files from `/usr/share/kbd/consolefonts`.

{{< listdir path="files/readme" >}}


## Issues

The screenshots for [solar24x32.psfu](#solar24x32psfu) and [latarcyrheb-sun32.psfu](#latarcyrheb-sun32psfu)
overflow the framebuffer resolution.
The Linode GLISH console only supports a resolution of 1280x768.  
https://www.linode.com/community/questions/11069/glish-resolution

Some day I might try with a local VM with a higher resolution framebuffer.

The [972.cp (8)](#972cp8) font is buggy.
The glyphs appear completely blank.


## Changelog

2012-08-05
: Initial upload.

2019-12-08
: Migrate and reformat to new blog engine.

2022-06-22
: Decouple this doc from my [personal blog](https://alexandre.deverteuil.net/).
  Migrate and reformat to a separate site.
  Use [docsy](https://www.docsy.dev/).
  Edit introduction.
  Update fonts screenshots and README files.


## Copying

Copyright &copy;  2012&ndash;2022  Alexandre de Verteuil.  
Permission is granted to copy, distribute and/or modify this document
under the terms of the GNU Free Documentation License, Version 1.3
or any later version published by the Free Software Foundation;
with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
A copy of the license is available at
[http://www.gnu.org/copyleft/fdl.html](http://www.gnu.org/copyleft/fdl.html).


## Screenshots

{{% screenshots %}}
