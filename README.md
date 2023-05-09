# Build app

Everything you need to build this Dapp

## Required

Install some [prerequisites](https://tauri.app/v1/guides/getting-started/prerequisites) and [NodeJS](https://github.com/nvm-sh/nvm) then do these steps:

```bash
# Install PNPM
npm i -g pnpm

# Install dependencies
pnpm i

```

## Developing

Once you've created a project and installed dependencies, start a development server:

```bash
pnpm tauri dev
```

## Building

To create a production version of your app:

```bash
npm tauri build
```
<!-- 
You can preview the production build with `npm run preview`.

> To deploy your app, you may need to install an [adapter](https://kit.svelte.dev/docs/adapters) for your target environment. -->
