
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from google.oauth2.credentials import Credentials


@dataclass
class SWAT:
    """Base object for SWAT."""

    @dataclass
    class CredStore:
        """Credentials store object."""

    config: dict
    cred_path: Path
    token_path: Path
    creds: Optional[Credentials] = field(default=None)
    cred_store: Optional[CredStore] = field(default_factory=CredStore)

    def add_creds(self, key, value):
        """Add a credential to the store."""
        setattr(self.cred_store, key, value)
