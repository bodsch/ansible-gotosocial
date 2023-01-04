
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


## Operating systems

Tested on

* Arch Linux
* Debian based
    - Debian 10 / 11
    - Ubuntu 20.10


## Contribution

Please read [Contribution](CONTRIBUTING.md)

## Development,  Branches (Git Tags)

The `master` Branch is my *Working Horse* includes the "latest, hot shit" and can be complete broken!

If you want to use something stable, please use a [Tagged Version](https://github.com/bodsch/ansible-gotosocial/tags)!

## Configuration

```yaml
gotosocial_version: 2.8.1

gotosocial_release_download_url: https://github.com/distribution/distribution/releases

gotosocial_system_user: gotosocial
gotosocial_system_group: gotosocial
gotosocial_config_dir: /etc/docker/gotosocial

gotosocial_direct_download: false

gotosocial_service: {}
gotosocial_log: {}
gotosocial_storage: {}
gotosocial_auth: {}
gotosocial_middleware: {}
gotosocial_reporting: {}
gotosocial_http: {}
gotosocial_notifications: {}
gotosocial_redis: {}
gotosocial_health: {}
gotosocial_proxy: {}
gotosocial_compatibility: {}
gotosocial_validation: {}
```

### `gotosocial_log`

[upstream doku](https://github.com/distribution/distribution/blob/main/docs/configuration.md#log)

```yaml
gotosocial_log:
  accesslog:
    disabled: true
  level: info
  formatter: text
  fields: {}
```

### `gotosocial_storage`

[upstream doku](https://github.com/distribution/distribution/blob/main/docs/configuration.md#storage)
```yaml
gotosocial_storage:
  filesystem:
    rootdirectory: /var/lib/gotosocial
    maxthreads: 100
  delete:
    enabled: false
  cache:
    blobdescriptorsize: 10000

```

### `gotosocial_auth`

[upstream doku](https://github.com/distribution/distribution/blob/main/docs/configuration.md#auth)
```yaml
gotosocial_auth: {}
```

### `gotosocial_middleware`

[upstream doku](https://github.com/distribution/distribution/blob/main/docs/configuration.md#middleware)
```yaml
gotosocial_middleware: {}
```

### `gotosocial_reporting`

[upstream doku](https://github.com/distribution/distribution/blob/main/docs/configuration.md#reporting)
```yaml
gotosocial_reporting: {}
```

### `gotosocial_http`

[upstream doku](https://github.com/distribution/distribution/blob/main/docs/configuration.md#http)
```yaml

gotosocial_http:
  addr: localhost:5000
  secret: "{{ ansible_host | b64encode }}"
  relativeurls: true
  debug:
    addr: localhost:5001
    prometheus:
      enabled: true
      path: /metrics
```

### `gotosocial_notifications`

[upstream doku](https://github.com/distribution/distribution/blob/main/docs/configuration.md#notifications)
```yaml
gotosocial_notifications: {}
```

### `gotosocial_redis`

[upstream doku](https://github.com/distribution/distribution/blob/main/docs/configuration.md#redis)
```yaml
gotosocial_redis: {}
```

### `gotosocial_health`

[upstream doku](https://github.com/distribution/distribution/blob/main/docs/configuration.md#health)
```yaml
gotosocial_health: {}
```

### `gotosocial_proxy`

[upstream doku](https://github.com/distribution/distribution/blob/main/docs/configuration.md#proxy)

```yaml
gotosocial_proxy: {}
```

### `gotosocial_compatibility`

[upstream doku](https://github.com/distribution/distribution/blob/main/docs/configuration.md#compatibility)
```yaml
gotosocial_compatibility: {}
```

### `gotosocial_validation`

[upstream doku](https://github.com/distribution/distribution/blob/main/docs/configuration.md#validation)
```yaml
gotosocial_validation: {}
```


---

## Author and License

- Bodo Schulz

## License

[Apache](LICENSE)

`FREE SOFTWARE, HELL YEAH!`
