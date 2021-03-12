def test_file_exists(host):
    snipeit = host.file('/snipeit.yml')
    assert snipeit.exists
    assert snipeit.contains('your')

# def test_snipeit_is_installed(host):
#     snipeit = host.package('snipeit')
#     assert snipeit.is_installed
#
#
# def test_user_and_group_exist(host):
#     user = host.user('snipeit')
#     assert user.group == 'snipeit'
#     assert user.home == '/var/lib/snipeit'
#
#
# def test_service_is_running_and_enabled(host):
#     snipeit = host.service('snipeit')
#     assert snipeit.is_enabled
#     assert snipeit.is_running
