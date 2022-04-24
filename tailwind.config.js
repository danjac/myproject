/* eslint-disable */

module.exports = {
    mode: 'jit',
    darkMode: 'media',
    future: {
        removeDeprecatedGapUtilities: true,
        purgeLayersByDefault: true,
    },
    content: [
        './myproject/templates/**/*.html',
        './myproject/static/js/**/*.js',
        // './tailwind-safelist.txt',
    ],
    keyframes: true,
    variants: {
        textColor: ['responsive', 'hover', 'focus', 'visited', 'dark'],
    },
    plugins: [
        require('@tailwindcss/forms'),
        // require('@tailwindcss/typography'),
        // require('@tailwindcss/line-clamp'),
    ],
};
