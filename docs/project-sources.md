# Project evidence

Reviewed on October 25, 2026. Sources were read from the public `djamespi` repositories through GitHub's public API and raw source endpoints. The GitHub plugin was not connected. Source projects were inspected, not executed.

## TeknoCare

- [Repository](https://github.com/djamespi/TeknoCare) and [contributors](https://api.github.com/repos/djamespi/TeknoCare/contributors): owned by `djamespi`, who appears in contributor metadata.
- [Dependencies](https://github.com/djamespi/TeknoCare/blob/main/requirements.txt): Django and PostgreSQL driver.
- [Registration view](https://github.com/djamespi/TeknoCare/blob/main/apps/register/views.py): registration form processing and redirect to sign-in.
- [Profile model](https://github.com/djamespi/TeknoCare/blob/main/apps/profile/models.py): user-linked profile fields.
- [JOIN queries](https://github.com/djamespi/TeknoCare/blob/main/apps/joins/queries.py): parameterized INNER/LEFT JOIN demonstrations and result checks. The tree also includes HTML templates and CSS.

The entry describes implemented source features, without claiming a production clinic deployment or measured outcomes.

## Habitually

- [Repository and README](https://github.com/djamespi/Habitually) and [contributors](https://api.github.com/repos/djamespi/Habitually/contributors): owned by `djamespi`, who appears in contributor metadata; the README describes a habit tracker and Tailwind styling.
- [Project file](https://github.com/djamespi/Habitually/blob/main/Habitually/Habitually.csproj): C#, .NET, Blazor WebAssembly.
- [Habit service](https://github.com/djamespi/Habitually/blob/main/Habitually/Services/HabitService.cs): habit creation, edits, deletion, completion toggling, and in-memory state.
- [Streak calculator](https://github.com/djamespi/Habitually/blob/main/Habitually/Services/StreakCalculator.cs): current and longest streak calculations.

The portfolio explicitly notes that data resets on reload. It makes no claim of persistent storage or a completed Insights page.

## CS345 backpropagation activity

- [Repository](https://github.com/djamespi/CS345---BackProp-Activity) and [contributors](https://api.github.com/repos/djamespi/CS345---BackProp-Activity/contributors): owned by `djamespi`, who appears in contributor metadata.
- The repository contains an original C# program and a modified version named `BackPropProgram with CrossEntropy and WeightDecay (modified file).cs`.
- The modified version includes a cross-entropy/MSE switch, a weight-decay training parameter, L2 penalty calculation, generated training data, and training/test accuracy output.

The entry presents this as an extension of supplied coursework code. No numeric accuracy or improvement is claimed because the program was not run during this portfolio task.
