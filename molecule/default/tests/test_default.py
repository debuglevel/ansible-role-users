import datetime as dt

"""Role testing files using testinfra."""


def test_updated(host):
    """Validate files updated"""

    files_names = [
        "/etc/group",
        "/etc/passwd",
        "/etc/shadow",
        ]

    for file_name in files_names:
        file = host.file(file_name)

        now = dt.datetime.today()

        assert file.exists
        assert (now - file.mtime).total_seconds() < 600

# def test_groups(host):
#     """Validate group in /etc/group"""

#     f = host.file("/etc/group")
#     #print(f.content)
#     assert f.contains("testgroup:x:")
#     assert f.contains(":1138:")
#     assert f.contains(":testuser")
#     #assert f.contains("testgroup:x:1138:testuser")  # the users' main group is not in /etc/group
#     assert f.contains("testgroup:x:1138:")
#     assert f.contains("audio:.*testuser")
#     assert f.contains("games:.*testuser")

def test_users(host):
    """Validate user in /etc/passwd"""

    f = host.file("/etc/passwd")
    assert f.contains("testuser:x:")
    assert f.contains(":4711:")
    assert f.contains(":10:")
    assert f.contains(":/home/testuser:")
    assert f.contains(":/bin/bash")
    assert f.contains("testuser:x:4711:10:.*:/home/testuser:/bin/bash")

def test_shadow(host):
    """Validate user in /etc/shadow"""

    f = host.file("/etc/shadow")
    assert f.contains("testuser:")

def test_authorized_keys(host):
    """Validate user in /home/testuser/.ssh/authorized_keys"""

    f = host.file("/home/testuser/.ssh/authorized_keys")
    print(f.content)
    assert f.exists
    assert f.contains("ssh-ed25519 ABCDEFG comment text")
    assert f.contains("ssh-rsa HIJKLMN comment text")

# def test_directories(host):
#     """Validate service directories exists."""
#     directories = [
#     ]

#     for directory in directories:
#         d = host.file(directory)

#         assert d.exists
#         assert d.is_directory

# def test_files(host):
#     """Validate files existing"""

#     files_names = [
#     ]

#     for file_name in files_names:
#         file = host.file(file_name)

#         assert file.exists
#         assert file.is_file

# TODO: Does not seem to work on molecule.
# def test_service(host):
#     """Validate service is valid."""
#     service = host.service("template")
#
#     assert service.is_valid

# def test_commands(host):
#     """Validate commands exists."""
#     commands = [
#     ]

#     for command in commands:
#         c = host.find_command(command)

# def test_executables(host):
#     """Validate service executables exists."""
#     executables = [
#     ]
#
#     for executable in executables:
#         e = host.file(executable)
#
#         assert e.exists
#         assert e.is_file
#         assert e.is_executable
