import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_asciinema_package_installed(host):
    assert host.package("asciinema").is_installed


def test_asciinema_binary_exists(host):
    assert host.file('/usr/bin/asciinema').exists


def test_asciinema_binary_file(host):
    assert host.file('/usr/bin/asciinema').is_file


def test_asciinema_binary_which(host):
    assert host.check_output('which asciinema') == \
      '/usr/bin/asciinema'
