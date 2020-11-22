import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE = 'asciinema'
PACKAGE_BINARY = '/usr/bin/asciinema'


def test_asciinema_package_installed(host):
    """
    Tests if asciinema package is installed.
    """
    assert host.package(PACKAGE).is_installed


def test_asciinema_binary_exists(host):
    """
    Tests if asciinema binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_asciinema_binary_file(host):
    """
    Tests if asciinema binary is a file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_asciinema_binary_which(host):
    """
    Tests the output to confirm asciinema's binary location.
    """
    assert host.check_output('which asciinema') == PACKAGE_BINARY
