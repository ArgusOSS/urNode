# The why's and how's

These yaml configurations are loaded up into your k8s server and then launched accordingly as you interact with the urNode backend. The network ports might be edited on the fly however with of course, you having the option to change it for the sake of ease of use. The changed config would be dumped to the database and saved for future reference.

The point of letting these yaml configurations stay in one directory per chain to make it easier for you to use them separately if you wish to or change them as you like. However, in the future, better support for such deployments would be provided as the project matures.
