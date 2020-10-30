from django.db.models.lookups import IExact
from encrypted_fields.fields import SearchField


class SearchFieldAllowIExact(SearchField):
    """
    A search field that allow the usage of IExact search.

    WARNING: Use with caution. This option was disabled normally in django-searchable-encrypted-fields.
    Using this field might cause some unexpected behaviour.
    """
    pass


SearchFieldAllowIExact._unregister_lookup(IExact)
