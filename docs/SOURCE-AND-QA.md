# Content provenance and quality checklist

Original page: https://psalm-23-transportation.igarza5652.chatgpt.site/

Reviewed 2026-10-14. The source was a single-page site titled "Psalm 23 Transportation | Anything. Anywhere." with `What we haul`, `Our story`, and `Request a quote` sections. The recreated page retains its service descriptions, family story, scripture, and contact information in `content/site.json`, and uses the original text-based quote initiation. No unsupported licensing, service-area or load-capacity assertions were added.

The source logo is a JPEG at `https://psalm-23-transportation.igarza5652.chatgpt.site/logo.jpeg`. Because the file itself was not downloadable in the build environment, the recreation references that existing source URL and supplies an original SVG fallback. Replacing the URL with the business's approved uploaded logo is a recommended launch step. Additional vector illustrations in `public/assets` are independently authored placeholders, not certified likenesses of a particular owned vehicle.

## Checks before going live

- [ ] Confirm the family story wording with the business owner.
- [ ] Confirm that `281-766-1320` is the correct SMS and voice contact number.
- [ ] Confirm that `Psalm23Transportation@yahoo.com` receives quote requests.
- [ ] Upload the approved source logo so it is hosted with the new site.
- [ ] Verify the exact destinations/routes, trailer specifications and regulatory status independently before adding any claims.
- [ ] Verify contrast, keyboard focus, mobile navigation, and form validation on the deployed site.
- [ ] Confirm quote form SMS behaviour on iOS and Android, and email fallback on desktop.
- [ ] Confirm unapproved GitHub accounts cannot sign in.
- [ ] Confirm draft, publish and GitHub workflow execution end to end.
- [ ] Confirm correct domain/HTTPS after DNS propagation.

## Local verification completed for the draft

`npm run verify` exercises schema validation, HTML escaping, media URL restrictions, contact data consistency, CMS collection wiring, a valid Worker OAuth authorization redirect, signed cookie checks, and rejection of invalid state/unconfigured access. The local environment cannot certify the final GitHub/Cloudflare live configuration without the new repository and OAuth credentials.
