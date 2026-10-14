# Psalm 23 Transportation — Website & Editor

A polished, responsive recreation of the public-facing **Psalm 23 Transportation** single-page website. It includes a separately hosted administration interface, designed around the same architecture as the Thrive PTO project: **Decap CMS, GitHub content storage, GitHub Pages deployment, and a Cloudflare Worker for GitHub OAuth sign-in**.

The content and contact details were transcribed from the source page supplied by the client. Visual styling is an original recreation, not a guaranteed pixel-perfect copy of the source CSS. The original logo is currently linked from the reference site until an approved local image is uploaded.

## What's included

- Homepage with editable hero, service cards, family story, scripture, and quote request form.
- Working click-to-text, click-to-email and copy-request actions (the visitor reviews and sends the message in their own app; no form database or silent submission).
- Responsive mobile navigation and accessible form fields.
- Form-based CMS editor at `/admin/`: text, images, services, colors, phone, email, and all labels.
- Draft and publish workflow backed by GitHub's version history.
- Cloudflare Worker OAuth with state + PKCE verification, secure cookies, GitHub user allowlists, and repository permission checks.
- GitHub Actions build/publish workflow and dependency-free site build/tests.

## Start here

1. Open `docs/SETUP.md` for the GitHub Pages + Cloudflare setup steps.
2. Open `dist/index.html` locally for a static preview. No CMS sign-in is available until GitHub and Cloudflare are connected.
3. After deployment visit `https://YOUR-DOMAIN/admin/` for editor access.

**Do not upload this into the Thrive PTO repository.** Create a separate repository for this business.

## Run locally

Requirements: Node 22 or newer. The build process has **no npm dependencies**.

```sh
npm run verify
```

The generated static site is in `dist/`. For local testing with correct asset paths:

```sh
python -m http.server --directory dist 8000
```

Then open `http://localhost:8000/`. The public website functions locally; GitHub editing requires deployment and live OAuth configuration. Opening `index.html` directly also displays the site, although browser security may limit some features in `file://` mode.

## Structure

```text
content/site.json          Editable source content (all page fields)
public/assets/            CSS, site JavaScript and replaceable SVG artwork
public/admin/             Decap editor, user guide and history instructions
scripts/                  Build, CMS config and validation
cms/oauth/                Secure GitHub login Worker
cms/setup.json            Repository and OAuth URL placeholders (no secrets)
.github/workflows/        GitHub Pages deployment
docs/                     Handover and deployment instructions
dist/                     Pre-built, GitHub Pages-ready public output
```

All CMS credentials are set in Cloudflare secrets. No client secret should ever be committed to a repository, embedded in the HTML, or sent to the end user's browser. The GitHub token is sent by OAuth only to the approved Decap CMS origin.

## Original content

Source: https://psalm-23-transportation.igarza5652.chatgpt.site/ (reviewed October 14, 2026).

The source page has the business phone number `281-766-1320`, contact address `Psalm23Transportation@yahoo.com`, and a logo served at `/logo.jpeg`. Because the logo's binary file could not be retrieved in this environment, the new site uses the source site's HTTPS logo URL initially, plus a bundled original fallback mark. **Upload the approved logo in the CMS to remove that dependency**.

## Limitations before activation

- Live editor login cannot be verified until your GitHub repo, GitHub OAuth app, Cloudflare Worker, and permitted users are configured.
- CMS JavaScript is pinned to Decap CMS 3.16.3 and loaded from unpkg; this is an internet dependency for the editor only. The public site does not depend on Decap or on the login Worker.
- The website's quote form mirrors the original handoff-to-text approach and does not create tickets or deliver submissions automatically.
- A future custom domain and verified ownership of the source logo are not assumed.


## Deployment correction — Psalm23

The canonical repository is `macv0223/Psalm23` at `https://github.com/macv0223/Psalm23`. The public site is `https://macv0223.github.io/Psalm23/`. Static files from `dist/` are mirrored to the repository root for compatibility with **Deploy from a branch → main → /(root)**. The included `.github/workflows/pages.yml` is the recommended ongoing publisher: in **Settings → Pages**, change **Source** to **GitHub Actions** and run the publish workflow. Otherwise content edits saved through the CMS do not automatically rebuild the root mirror. The CMS sign-in also requires a separate configured Cloudflare Worker and GitHub OAuth app.


## Fix for macv0223/Psalm23 GitHub Pages

This package includes an `index.html` and complete `assets/`, `admin/`, and `data/` at the repository ROOT, in addition to the original `dist/` build. For branch-based hosting, select **Settings > Pages > Deploy from a branch > main > /(root)**.

The hidden `.github/workflows/pages.yml` has also been included for automatic CMS publishing. For this preferred long-term mode, instead select **GitHub Actions** in **Settings > Pages > Build and deployment > Source**. This must be selected by a repository administrator; simply including the workflow does not change the Pages Source setting. The editor is not live until Cloudflare OAuth is separately configured.
