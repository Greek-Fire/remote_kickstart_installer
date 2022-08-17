theforeman.foreman.locations
================================

This role creates and manages locations. 

Role Variables
--------------

This role supports the [Common Role Variables](https://github.com/theforeman/foreman-ansible-modules/blob/develop/README.md#common-role-variables).

The main data structure for this role is the list of `foreman_locationss`. Each `organization` requires the following fields:

- `name`: The name of the location.

The following fields are optional in the sense that the server will use default values when they are omitted:

- `description`: The description of the organization.
- `state`: The state of the organization. Can be `present` or `absent`.

Example Playbooks
-----------------

```yaml
--- 
- name: add location to foreman
  hosts: localhost
  gather_facts: false
  roles:
    - role: theforeman.foreman.locations
      vars: 
        foreman_server_url: https://foreman.example.com
        foreman_username: admin
        foreman_password: changeme
        foreman_locations:
          - name: raleigh
            state: present
          - name: default
            state: absent
            description: pacific datacenter 
```
