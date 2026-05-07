# Vishwanath Construction Website Resource Plan

## Goal
Provide a clear resource inventory and implementation plan for turning the current prototype into a fully production-ready, international-level construction website.

## Required Assets
1. Design assets
   - High-resolution hero video or image (modern villa architecture)
   - Room lifestyle imagery for living room, bedroom, balcony, garden
   - Client project before/after photography (real Patna projects)
   - Icon set (line/filled style in gold/black tones)
   - Logo files (SVG + PNG variations)
   - 3D villa model assets (additional textures, animations, interactive labels) - CAD-style interface implemented

2. Content assets
   - Final copy for each section (incl. FAQ, About, Trust messages)
   - SEO metadata per page (title, description, keywords)
   - Testimonials with names + photos (consent approved)
   - Portfolio project case studies (text and images)

3. Technical resources
   - CDN for assets (images/fonts) and media compression pipeline
   - Form processing backend or service (e.g., Netlify Forms, Formspree)
   - Google Maps embed API key for contact page
   - WhatsApp business link with company number
   - Analytics (Google Analytics, tag manager)

4. Copy and legal
   - Privacy policy text (data collection and use)
   - Terms and conditions page text
   - Company accreditation / certifications for trust section

## Enhancement components
- Mobile-first responsive framework and testing matrix (Chrome, Safari, Firefox, Edge on iOS/Android)
- Performance / accessibility checks (Lighthouse, Axe)
- Progressive enhancements:
  - smooth scroll and parallax  - 3D building simulator (interactive cube) for rooms and levels  - sticky navigation and floating CTA
  - live testimonial slider and animated counters
  - project before/after swiper

## Implementation steps
1. Replace Unsplash placeholders with real brand images.
2. Add real navigation links + remove placeholder pages if not used.
3. Wire contact form to backend service and verify data flow.
4. Set up caching headers and static site hosting (Netlify, Vercel, AWS S3).
5. Add i18n or Hreflang if required for local language support.

---
`resource-plan.md` updates the plan and can be used as a foundation for development and handover.
