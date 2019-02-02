# 🛠️▶️ Powerline Xcode Version Segment

Powerline status prompt segment which displays the active version of Xcode.

[![PyPI version](https://badge.fury.io/py/powerline-xcodeversion.svg)](https://badge.fury.io/py/powerline-xcodeversion)

# 🤳🏻 Usage

Add the `xcodeversion` snippet below to your powerline theme JSON file.

```diff
{
    "segments": {
        "left": [
+            {
+                "function": "powerline_xcodeversion.xcodeversion",
+                "priority": 60
+            },
            ...
```

## 🔧 Configuration

The spacing and symbol in the xcodeversion section can be customized (or removed).
Add the following to your main
[`powerline/config.json`](https://powerline.readthedocs.io/en/master/configuration.html)
file:

```diff
{
    "segment_data": {
+        "xcodeversion": {
+            "args": {
+                "format": "🛠  {}"
+            }
+        },
        ...
```

The example above shows the default format.
The `{}` will be replaced with the version number.

💡 Remember to kill the powerline daemon with `powerline-daemon -k`
so that your changes will show up immediately while you test configuration changes.

# 📄 License

This repo is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for rights and limitations.
