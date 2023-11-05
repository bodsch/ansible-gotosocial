
# Ansible Role:  `gotosocial` 

Ansible role to install and configure [gotosocial](https://github.com/superseriousbusiness/gotosocial).

[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/bodsch/ansible-gotosocial/main.yml?branch=main)][ci]
[![GitHub issues](https://img.shields.io/github/issues/bodsch/ansible-gotosocial)][issues]
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/bodsch/ansible-gotosocial)][releases]
[![Ansible Quality Score](https://img.shields.io/ansible/quality/50067?label=role%20quality)][quality]

[ci]: https://github.com/bodsch/ansible-gotosocial/actions
[issues]: https://github.com/bodsch/ansible-gotosocial/issues?q=is%3Aopen+is%3Aissue
[releases]: https://github.com/bodsch/ansible-gotosocial/releases
[quality]: https://galaxy.ansible.com/bodsch/gotosocial

If `latest` is set for `gotosocial_version`, the role tries to install the latest release version.  
**Please use this with caution, as incompatibilities between releases may occur!**

The binaries are installed below `/usr/local/bin/gotosocial/${gotosocial_version}` and later linked to `/usr/bin`. 
This should make it possible to downgrade relatively safely.

The Archive is stored on the Ansible controller, unpacked and then the binaries are copied to the target system.
The cache directory can be defined via the environment variable `CUSTOM_LOCAL_TMP_DIRECTORY`. 
By default it is `${HOME}/.cache/ansible/gotosocial`.
If this type of installation is not desired, the download can take place directly on the target system. 
However, this must be explicitly activated by setting `gotosocial_direct_download` to `true`.

## Requirements & Dependencies

Ansible Collections

- [bodsch.core](https://github.com/bodsch/ansible-collection-core)
- [bodsch.scm](https://github.com/bodsch/ansible-collection-scm)

```bash
ansible-galaxy collection install bodsch.core
ansible-galaxy collection install bodsch.scm
```
or
```bash
ansible-galaxy collection install --requirements-file collections.yml
```

## Operating systems

Tested on

* Arch Linux
* Debian based
    - Debian 10 / 11 / 12
    - Ubuntu 20.10 / 22.04


## Contribution

Please read [Contribution](CONTRIBUTING.md)

## Development,  Branches (Git Tags)

The `master` Branch is my *Working Horse* includes the "latest, hot shit" and can be complete broken!

If you want to use something stable, please use a [Tagged Version](https://github.com/bodsch/ansible-gotosocial/tags)!

## Configuration

```yaml
gotosocial_version: 0.6.0

gotosocial_release_download_url: https://github.com/superseriousbusiness/gotosocial/releases

gotosocial_system_user: gotosocial
gotosocial_system_group: gotosocial
gotosocial_config_dir: /etc/gotosocial
gotosocial_data_dir: /var/lib/gotosocial

gotosocial_direct_download: false

gotosocial_service: {}
gotosocial_config: {}
```


https://docs.gotosocial.org/en/latest
https://github.com/superseriousbusiness/gotosocial

---

## Author and License

- Bodo Schulz

## License

[Apache](LICENSE)

**FREE SOFTWARE, HELL YEAH!**
