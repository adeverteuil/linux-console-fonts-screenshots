# Linux Console Fonts site


## Build prerequisites

https://www.docsy.dev/docs/get-started/docsy-as-module/installation-prerequisites/

* An Archlinux VM
* Ansible
* Hugo Extended >=v0.73.0.
* Go >=v1.12
* Recent NodeJS
  * Install from [nodesource](https://github.com/nodesource/distributions/blob/master/README.md),
    the version that is in the Ubuntu 20.04 repository is too old (version 10 or something).
* PostCSS (NPM module)
  ```
  cd hugo-site
  npm install -D autoprefixer
  npm install -D postcss-cli
  npm install -D postcss
  ```


## Generating the screenshots

1. Create a Linode VM:
   * Size: Nanode 1GB
   * 1 CPU core
   * 25 GB storage
1. CD into the `ansible` directory.
1. Update the inventory file.  
   Copy `hosts.example` to `hosts` and edit it.
1. Run the `playbook.yml` playbook.
   ```
   ansible-playbook playbook.yml
   ```


## Generating/updating the screenshots

1. Go to the project root.
1. SCP the files.
   ```
   rsync --recursive --delete root@your-linode:screenshots hugo-site/static
   ```
1. Download the YAML data.
   ```
   scp root@your-linode:fonts.yaml hugo-site/data/fonts.yaml
   ```


## Developing the website (serving locally)

Do steps 1 to 3 above and use the `dev-server.sh` command to serve the site locally.

```
./dev-server.sh
```


## Generating/updating the site

1. Generate the site.
   ```
   ./generate-site.sh
   ```
1. Create a PR or push to the `main` branch.


## Docsy customizations

* Installed [lazysizes](https://github.com/aFarkas/lazysizes) in `static/scripts/lazysizes.min.js`.
* Loaded lazysizes in `/layouts/partials/hooks/head-end.html` ([documentation](https://www.docsy.dev/docs/adding-content/lookandfeel/#customizing-templates)).
* Created a `screenshots` shortcode in `/layouts/shortcodes/screenshots.html`.


## To do

Site:

* [ ] Edit GitHub repo URL.
* [ ] Figure out hosting and domain name.
      * GitHub pages?
* [ ] Edit Introduction with description of my process.
* [ ] Update link on Archlinux wiki.
* [ ] Set up Matomo site.
      * [ ] Make sure it is only added on my build, not in GitHub.
* [ ] Update tarball, host it in static.
* [ ] Redirect old URL from my blog to the new site.
* [ ] Move Readme files from my static site to this site.

Repository:

* [X] Create Ansible playbook.
      * Install required packages: `fbdump`, `netpbm`, `libpng`.
* [X] Create a shortcode and use YAML data

Script:

* [X] Fix error in the script.
* [ ] Modernize the script.
      * [ ] Use `argparse`.
* [ ] Generate tarball, host it in `static`.
