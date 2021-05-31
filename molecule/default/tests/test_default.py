import pytest
import os
import yaml
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.fixture()
def AnsibleDefaults(Ansible):
    with open("../../../defaults/main.yml", 'r') as stream:
        return yaml.load(stream)


@pytest.mark.parametrize("dirs_debian", [
    "/etc/gitlab-runner"
])
@pytest.mark.parametrize("dirs_redhat", [
    "/etc/gitlab-runner"
])
def test_directories(host, dirs_debian, dirs_redhat):
    if host.system_info.distribution == 'debian':
        d = host.file(dirs_debian)
        assert d.is_directory
        assert d.exists
    if host.system_info.distribution == 'redhat':
        d = host.file(dirs_redhat)
        assert d.is_directory
        assert d.exists
    

@pytest.mark.parametrize("files_debian", [
    "/etc/gitlab-runner/config.toml"
])
@pytest.mark.parametrize("files_redhat", [
    "/etc/gitlab-runner/config.toml"
])
def test_files(host, files_debian, files_redhat):
    if host.system_info.distribution == 'debian':
        f = host.file(files_debian)
        assert f.exists
        assert f.is_file
    if host.system_info.distribution == 'redhat':
        f = host.file(files_redhat)
        assert f.exists
        assert f.is_file

@pytest.mark.parametrize("ports_debian", [
    "tcp://0.0.0.0:80"
])
@pytest.mark.parametrize("ports_redhat", [
    "tcp://0.0.0.0:80"
])
def test_socket(host, ports_debian, ports_redhat):
    if host.system_info.distribution == 'debian':
        s = host.socket(ports_debian)
        assert s.is_listening
    if host.system_info.distribution == 'redhat':
        s = host.socket(ports_redhat)
        assert s.is_listening