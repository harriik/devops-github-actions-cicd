from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
HTML_FILE = ROOT / "site" / "index.html"
CSS_FILE = ROOT / "site" / "style.css"


class WebsiteTests(unittest.TestCase):

    def test_homepage_exists(self):
        self.assertTrue(HTML_FILE.exists())

    def test_stylesheet_exists(self):
        self.assertTrue(CSS_FILE.exists())

    def test_heading_is_present(self):
        html = HTML_FILE.read_text(encoding="utf-8")
        self.assertIn(
            "CI/CD Pipeline with GitHub Actions",
            html
        )

    def test_stylesheet_is_linked(self):
        html = HTML_FILE.read_text(encoding="utf-8")
        self.assertIn('href="style.css"', html)


if __name__ == "__main__":
    unittest.main()
