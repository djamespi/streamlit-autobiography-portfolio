# Project evidence

Reviewed on October 25, 2026. Dexter selected CITUClinicSystem for technical work, tinHealth for backend development, and Parola for AI development. Features were checked against the repositories using existing GitHub access. The source projects were inspected, not executed.

## CITUClinicSystem — Technical

- [Repository](https://github.com/djamespi/CITUClinicSystem), branch `newBranch`.
- The source tree includes student, administrator, and provider dashboards; appointment and provider-schedule management; medical-record editing; support tickets; and audit-log views.
- [Appointment management](https://github.com/djamespi/CITUClinicSystem/blob/newBranch/manage_appointments.php) includes appointment cancellation, slot updates, and audit-log insertion.
- [Medical-history export](https://github.com/djamespi/CITUClinicSystem/blob/newBranch/export_medical_history.php) uses FPDF to produce a PDF from patient and medical-record queries.
- PHP, SQL, HTML, CSS, JavaScript, and FPDF are represented in source files.

Role wording follows Dexter's selection of this team project for technical work. It does not assign every feature to him individually or claim a production clinic deployment.

## tinHealth — Backend Development

- [Team repository and README](https://github.com/Gianne818/tinHealth), branch `main`.
- The README identifies Dexter James D. Benitez's role as backend, database operations, and some frontend work.
- [Maven configuration](https://github.com/Gianne818/tinHealth/blob/main/pom.xml) lists JavaFX, MySQL Connector/J, and Java compilation settings.
- Source files under `src/main/java/org/tin/oop2_capstone/database/` implement repository and data-source layers. Reviewed `UserRepository.java` and `MealRepository.java` expose user and meal operations.
- The README describes meal/activity logs, nutrition integration, exercise prompts, and user preferences. Its platform limitation is that exercise observation currently works only on macOS; the portfolio does not claim cross-platform support for that feature.

## Parola — AI Development

- [Team repository](https://github.com/Gianne818/AIHackathon2026_StarISDA_Parola), branch `main`. This repository is private. Its source link in the app explicitly requires access; no visibility changes were made.
- Dexter supplied the public display name **Parola** and selected this project for his AI-development work.
- The README describes a fisheries platform for municipal fisherfolk, with fishing-zone modeling, ocean data, a web portal, and SMS advisories.
- Reviewed notebook imports and model-construction lines confirm LightGBM models for pelagic and demersal work, pandas, NumPy, and scikit-learn/DBSCAN usage.
- Dependency lists and selected implementation files confirm Next.js/React, FastAPI, Supabase, ocean-grid processing, and habitat-suitability calculations.

The public portfolio contains a high-level project summary only. It does not copy the private repository's source, notebooks, data, assets, or credentials, and does not claim measured model accuracy or operational results. Role wording follows Dexter's supplied focus area rather than attributing specific team components to him alone.
