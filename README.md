[![Build Status](https://travis-ci.com/darkwizard242/ansible-role-asciinema.svg?branch=master)](https://travis-ci.com/darkwizard242/ansible-role-asciinema) ![Ansible Role](https://img.shields.io/ansible/role/43079?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/43079?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/43079?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-asciinema&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-asciinema) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-asciinema?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-asciinema?color=orange&style=flat-square)

# Ansible Role: asciinema

Role to install (_by default_) [asciinema](https://asciinema.org) or uninstall (_if passed as var_) on **Ubuntu** systems.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
asciinema_app: asciinema
asciinema_app_desired_state: present
asciinema_ubuntu_repo: 'ppa:zanchey/asciinema'
asciinema_ubuntu_repo_desired_state: present
asciinema_ubuntu_repo_filename: asciinema
```

### Variables table:

Variable                            | Value (default)         | Description
----------------------------------- | ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
asciinema_app                       | asciinema               | Defines the app to install i.e. **asciinema**
asciinema_package_desired_state     | present                 | Defined to dynamically chose whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package. Default is set to `present`.
asciinema_ubuntu_repo               | 'ppa:zanchey/asciinema' | Refers to the ppa repo to add. _Applies only to Ubuntu systems, not required for any other system._
asciinema_ubuntu_repo_desired_state | present                 | Defined to dynamically chose whether to add/keep (i.e. `present`) or remove (i.e. `absent`) the repository file list from `/etc/apt/sources.list.d`. _Applies only to Ubuntu systems, not required for any other system._
asciinema_ubuntu_repo_filename      | asciinema               | Defined to set the repository file name for saving in `/etc/apt/sources.list.d`. _Applies only to Ubuntu systems, not required for any other system._

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

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
