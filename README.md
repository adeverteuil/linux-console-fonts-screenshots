# Linux Console Fonts site

Source code for the site
[Linux Console Fonts Screenshots](https://adeverteuil.github.io/linux-console-fonts-screenshots/).


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
   Copy `host.example` to `hosts` and edit it.
1. Run the `playbook.yml` playbook.
   ```
   ansible-playbook playbook.yml
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

Playbook:

* [X] Update tarball, host it in static.
* [X] Download files automatically instead of the commands documented above.
* [X] Download/update Readme files automatically.
      * Would need a data file and a shortcode, just like screenshots.
      * Alternative: https://discourse.gohugo.io/t/list-files-in-a-directory/21258/3

Site:

* [X] Figure out hosting and domain name.
      * GitHub pages?
* [x] Edit GitHub repo URL.
* [X] Set up Matomo site.
      * [X] Add Matomo code in `head-end.html`.
* [X] Edit Introduction with description of my process.
* [X] Update Link to the Python script.
* [ ] Customized socials in footer.
* [X] Test and update GitHub repo link.
* [X] Migrate Readme files from my static site to this site.
* [X] Add a link back to my blog.
* [ ] Redirect old URL from my blog to the new site.
* [ ] Update link on Archlinux wiki.

Repository:

* [X] Create Ansible playbook.
      * Install required packages: `fbdump`, `netpbm`, `libpng`.
* [X] Create a shortcode and use YAML data

Script:

* [X] Fix error in the script.
* [ ] Modernize the script.
      * Use `argparse`.
      * Break out nested code blocks into separate functions.
* [ ] Investigate fonts screenshots that come out weird.
      * solar24x32.psfu
      * latarcyrheb-sun32.psfu
      * It's currently not possible to change the GLISH console resolution.  
        https://www.linode.com/community/questions/11069/glish-resolution
