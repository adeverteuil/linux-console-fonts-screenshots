# Linux Console Fonts site

## Generating the screenshots

1. Create a Linode VM:
   * Size: Nanode 1GB
   * 1 CPU core
   * 25 GB storage
1. CD into the `ansible` directory.
1. Update the inventory file.  
   Copy `hosts.example` to `hosts` and edit it.
1. Run the `setup.yml` playbook.
   ```
   ansible-playbook setup.yml
   ```


## Generating the website

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

Do steps 1 to 3 above and use this `hugo server` command to serve the site locally.

```
hugo server --cacheDir "$PWD/hugo_cache"
```


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

Repository:

* [X] Create Ansible playbook.
      * Install required packages: `fbdump`, `netpbm`, `libpng`.
* [X] Create a shortcode and use YAML data

Script:

* [ ] Fix error in the script.
* [ ] Modernize the script.
      * [ ] Use `argparse`.
* [ ] Generate tarball, host it in `static`.
