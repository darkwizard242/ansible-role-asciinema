[![build-test](https://github.com/darkwizard242/ansible-role-asciinema/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-asciinema/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-asciinema/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-asciinema/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/47641?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/47641?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/47641?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-asciinema&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-asciinema) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-asciinema&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-asciinema) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-asciinema&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-asciinema) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-asciinema&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-asciinema) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-asciinema?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-asciinema?color=orange&style=flat-square)

# Ansible Role: asciinema

Role to install (_by default_) [asciinema](https://asciinema.org) or uninstall (_if passed as var_) on **Debian** family and **EL** family systems

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
asciinema_app: asciinema
asciinema_app_desired_state: present
```

### Variables table:

Variable                        | Description
------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------
asciinema_app                   | Defines the app to install i.e. **asciinema**
asciinema_package_desired_state | Defined to dynamically chose whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package. Default is set to `present`.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **asciinema** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.asciinema
```

For customizing behavior of role (i.e. installation of latest **asciinema** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.asciinema
  vars:
    asciinema_package_desired_state: latest
```

For customizing behavior of role (i.e. un-installation of **asciinema** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.asciinema
  vars:
    asciinema_package_desired_state: absent
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-asciinema/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/).
